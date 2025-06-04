from flask import Blueprint, request
from flask_login import login_required, current_user
from api.db.services.user_service import UserService, UserTenantService
from api.db.db_models import UserTenantRole
from api.utils.api_utils import get_json_result, get_data_error_result, validate_request
from api.utils import get_uuid
from api.db import StatusEnum

user_mgmt = Blueprint('user_management', __name__, url_prefix='/api/user_management')

@user_mgmt.route('/users', methods=['GET'])
@login_required
def list_users():
    try:
        users = UserService.model.select().where(UserService.model.status == StatusEnum.VALID.value)
        users_list = [user.to_dict() for user in users]
        return get_json_result(data=users_list)
    except Exception as e:
        return get_data_error_result(message=str(e))

@user_mgmt.route('/user', methods=['POST'])
@login_required
@validate_request('email', 'nickname', 'password')
def create_user():
    req = request.json
    email = req['email']
    nickname = req['nickname']
    password = req['password']

    existing_users = UserService.model.select().where(UserService.model.email == email)
    if existing_users:
        return get_data_error_result(message='User with this email already exists.')

    user_id = get_uuid()
    try:
        UserService.save(id=user_id, email=email, nickname=nickname, password=password, status=StatusEnum.VALID.value)
        # Assign default role as NORMAL in UserTenant
        UserTenantService.save(id=get_uuid(), user_id=user_id, tenant_id=user_id, role=UserTenantRole.NORMAL, status=StatusEnum.VALID.value, invited_by=current_user.id)
        return get_json_result(message='User created successfully.', data={'user_id': user_id})
    except Exception as e:
        return get_data_error_result(message=str(e))

@user_mgmt.route('/user/<user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    req = request.json
    try:
        UserService.update_user(user_id, req)
        return get_json_result(message='User updated successfully.')
    except Exception as e:
        return get_data_error_result(message=str(e))

@user_mgmt.route('/user/<user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    try:
        UserService.delete_user([user_id], update_user_dict={'status': 0})
        return get_json_result(message='User deleted successfully.')
    except Exception as e:
        return get_data_error_result(message=str(e))

@user_mgmt.route('/user/<user_id>/roles', methods=['GET'])
@login_required
def get_user_roles(user_id):
    try:
        roles = UserTenantService.model.select().where(
            (UserTenantService.model.user_id == user_id) & (UserTenantService.model.status == StatusEnum.VALID.value)
        )
        roles_list = [role.to_dict() for role in roles]
        return get_json_result(data=roles_list)
    except Exception as e:
        return get_data_error_result(message=str(e))

@user_mgmt.route('/user/<user_id>/roles', methods=['POST'])
@login_required
def add_user_role(user_id):
    req = request.json
    tenant_id = req.get('tenant_id')
    role = req.get('role')
    if not tenant_id or not role:
        return get_data_error_result(message='tenant_id and role are required.')

    try:
        UserTenantService.save(id=get_uuid(), user_id=user_id, tenant_id=tenant_id, role=role, status=StatusEnum.VALID.value, invited_by=current_user.id)
        return get_json_result(message='Role added successfully.')
    except Exception as e:
        return get_data_error_result(message=str(e))

@user_mgmt.route('/user/<user_id>/roles/<role_id>', methods=['DELETE'])
@login_required
def remove_user_role(user_id, role_id):
    try:
        UserTenantService.model.update(status=0).where(
            (UserTenantService.model.id == role_id) & (UserTenantService.model.user_id == user_id)
        ).execute()
        return get_json_result(message='Role removed successfully.')
    except Exception as e:
        return get_data_error_result(message=str(e))

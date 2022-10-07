from flask import request, redirect, url_for
from controllers.authentication_controller.forms import UserLoginForm
from db.db import db
from db.models.all import User
# from services.authentication_service import AuthenticateService
# authenticate_service = AuthenticateService()
import json

class AuthenticationController:
    # ログイン
    def post_login(self):
        # user: User = db.session.execute(db.select(User).order_by(User.name)).first()
        users: list[User] = db.session.query(User).all()
        # print(users[0].name)
        return '1'
        return users
        form = UserLoginForm(request.form)
        if not form.validate():
            return form.errors
        return '成功'
        #     return render_login(form=form, error='')

        # result = authenticate_service.login(
        #     form.username.data, form.password.data)
        # if not result['successed']:
        #     return render_login(form=form, error=result['message'])
        # return redirect(url_for('routes.get_index'))

    # ログアウト
    def get_logout(self):
        pass
        # authenticate_service.logout()
        # return redirect(url_for('routes.get_index'))
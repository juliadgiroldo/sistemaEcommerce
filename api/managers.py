from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class GerirUsuario(BaseUserManager):
    def validar_email(self, email):
        try:
            validate_email(email)
        except:
            raise ValueError(_("Insera um e-mail valido"))
        
    def criar_usuario(self,email, nome, cpf, celular, password, **extrafields):
        if email:
            email= self.normalize_email(email)
            self.validar_email(email)
        else:
            raise ValueError(_("email requerido"))
        if not nome:
            raise ValueError(_("nome requerido"))
        if not cpf:
            raise ValueError(_("cpf requerido"))
        if not celular:
            raise ValueError(_("celular requerido"))
        
        user=self.model(email=email, nome=nome, cpf=cpf, celular=celular)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def criar_superuser(self,email, nome, cpf, celular, password, **extrafields):
        extrafields.setdefault("staff", True)
        extrafields.setdefault("superUser", True)

        if extrafields.get("staff") is not True:
            raise ValueError(_("O campo deve ser verdadeiro para superUser"))

        if extrafields.get("superUser") is not True:
            raise ValueError(_("O campo deve ser verdadeiro para superUser"))

        user = self.criar_usuario(self,email, nome, cpf, celular, password, **extrafields)
        user.save(using=self._db)
        return user    
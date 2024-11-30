from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.exceptions import ValidationError
import re

def validate_tron_wallet_address(value: str):
    """
    Validator to check if a wallet address is a valid Tron blockchain address.
    Tron addresses must start with 'T' followed by 33 alphanumeric characters.
    """
    if not re.match(r"^T[a-zA-Z0-9]{33}$", value):
        raise ValidationError(
            f"{value} is not a valid Tron wallet address. "
            f"Tron wallet addresses must start with 'T' followed by 33 alphanumeric characters."
        )


class User(AbstractUser):
    wallet = models.CharField(max_length=34, validators=[validate_tron_wallet_address], unique=True)
    coins = models.PositiveIntegerField(default=0)

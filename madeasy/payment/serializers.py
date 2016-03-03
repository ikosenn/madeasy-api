from madeasy.common.serializers import AuditFieldsMixin
from madeasy.payment.models import (
    Payment
)


class PaymentSerializer(AuditFieldsMixin):
    class Meta:
        model = Payment

from rest_framework import serializers


class AuditFieldsMixin(serializers.ModelSerializer):
    """
    Injects the fields in the abstract base model as a model
    instance is being saved.
    """
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    created_by = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    def create(self, validated_data):
        """`created` and `created_by` are only mutated if they are null"""

        """
        `if not validated_data.get('created', None):`
        This is deprecated because created by has been changed to a
        read_only field in the serializer
        """
        user = self.context['request'].user
        validated_data['created_by'] = user
        validated_data['updated_by'] = user

        return self.Meta.model.objects.create(**validated_data)

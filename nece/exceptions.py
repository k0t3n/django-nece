class NonTranslatableFieldError(Exception):
    def __init__(self, field_name):
        self.field_name = field_name
        message = "{} is not in translatable fields".format(field_name)
        super(NonTranslatableFieldError, self).__init__(message)

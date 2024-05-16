from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp
from .const import (
    REGEX_FOR_SHORT, SHORT_LENGTH,
    ORIGINAL_LENGTH, LONG_LINK,
    OBLIGATORY_FIELD, LINK_IS_NOT_VALID,
    YOUR_SHORT_LINK, CREATE,
    REGEX_MESSAGE
)


class URLMapForm(FlaskForm):
    original_link: URLField = URLField(
        label=LONG_LINK,
        validators=[
            DataRequired(message=OBLIGATORY_FIELD),
            URL(message=LINK_IS_NOT_VALID),
            Length(max=ORIGINAL_LENGTH)
        ]
    )
    custom_id: StringField = StringField(
        label=YOUR_SHORT_LINK,
        validators=[
            Length(max=SHORT_LENGTH),
            Optional(),
            Regexp(
                regex=REGEX_FOR_SHORT,
                message=REGEX_MESSAGE
            )
        ]
    )
    submit: SubmitField = SubmitField(CREATE)

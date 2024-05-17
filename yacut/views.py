from . import app
from .const import REDIRECT_VIEW
from .forms import URLMapForm
from .models import URLMap

from flask import flash, redirect, render_template, url_for


@app.route('/', methods=['GET', 'POST'])
def index_view() -> str:
    form: URLMapForm = URLMapForm()

    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    try:
        new_url_map: URLMap = URLMap.create(
            original=form.original_link.data,
            short=form.custom_id.data
        )

        return render_template(
            'index.html',
            url=url_for(REDIRECT_VIEW, short=new_url_map.short,
                        _external=True),
            form=form
        )
    except RuntimeError as error:
        flash(error)
        return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_view(short: str):
    return redirect(URLMap.get(short, or_404=True).original)

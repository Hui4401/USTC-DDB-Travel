from flask import request, redirect, url_for


def redirect_back(default='index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        return redirect(target)
    return redirect(url_for(default, **kwargs))

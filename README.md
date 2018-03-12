# rexpress/web-res

Web resources be used in **http://regular.express**

![ScreenShot](http://regular.express/images/screenshot.png)



### Dependency

Web site is rendered with **[Jikji v0.5](https://github.com/Prev/jikji/tree/0.5)** (Static website generator based on RESTFul Server).

`jikji` use [Jinja2](http://jinja.pocoo.org/) template engine which is used in [Flask](http://flask.pocoo.org/).
You can see jinja template documentation on [here](http://jinja.pocoo.org/docs/dev/templates/).

Environment datas are loaded from repository [rexpress/environments](https://github.com/rexpress/environments).



### Directory and file roles

- URL rules, template path, and model data is described in `pages.xml`
- `config.json` is config of pathes, server_info, importing libraries.
- `ds.py`  and  `ext.py` are functions that proccess sharing and environement datas.
- Static resources like css, js, img are located in `assets` folder.
- Template files are located in `templates` folder.



###  Build

<del>[regular.express](http://regular.express) is built automatically for every hour by Jenkins.</del> Currently stopped.

Commits in the `master` branch will be reflected as soon as they are built.
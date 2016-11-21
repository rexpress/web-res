#rexpress/web-res

Web resources be used in **http://regular.express**

![ScreenShot](http://regular.express/images/screenshot.png)



### Dependency

Web site is rendered with **[Jikji](https://github.com/Prev/jikji)** (Static website generator based on RESTFul Server).

`jikji` use [Jinja2](http://jinja.pocoo.org/) template engine which is used in [Flask](http://flask.pocoo.org/).
You can see jinja template documentation on [here](http://jinja.pocoo.org/docs/dev/templates/).

Environment datas are loaded from [rexpress/environments](https://github.com/rexpress/environments).



### Directory and file roles

- URL rules, template path, and model data is described in `pages.xml`
- `config.json` is config of pathes, server_info, importing libraries.
- `ds.py`  and  `ext.py` are functions that proccess sharing and environement datas.
- Static resources like css, js, img are located in `assets` folder.
- Template files are located in `templates` folder.



###  Build

[regular.express](http://regular.express) is built automatically for every hour by Jenkins.

Commits in the `master` branch will be reflected as soon as they are built.
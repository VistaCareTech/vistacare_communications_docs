# Vistacare Communications Docs

This is the repository for the documentation of the developments builded on VistaCare Communications.

## Online Documentation

https://gentle-ground-0bd1c310f.3.azurestaticapps.net/

## Requirements installation

To install the Python requirements excecute the following command.

```python
pip install -r requirements.txt
```

***Remember be on the root folder of the documentation***

## Compile the documentation

To compile the documentation run the following command:

```bash
sphinx-build -b html ./docs ./docs/_build --keep-going --no-color -w /tmp/sphinx-log
```

***To visualize the documentation go to the folder _build and open the index.html on your Browser.***

## Style guide

1. Tip

![](docs/_static/tip.png)

```html
<div class="seealso">
<p class="admonition-title">TIP</p>
<p>VistaCare Communications Plugin Docs.</p>
</div>
```


2. Alert

![](docs/_static/warning.png)

```html
<div class="warning">
<p class="admonition-title">WARNING</p>
<p>VistaCare Communications Plugin Docs.</p>
</div>
```

3. Important

![](docs/_static/important.png)

 ```html
<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>VistaCare Communications Plugin Docs.</p>
</div>
```

4. Images

It is necessary to use PNG or GIF to shows the functionality to the user.

The following code shows the GIF in the correct format on the documentation:

```html
<a class="" data-lightbox="QGIS Install" href="_static/install_qgis.gif" title="QGIS Install" data-title="QGIS Install"><img src="_static/install_qgis.gif" class="align-center" width="800px" height="500px" alt="QGIS Install">
</a>
```

Recommended parameters:

* Resolution: 1024 x 576
* FPS: 10

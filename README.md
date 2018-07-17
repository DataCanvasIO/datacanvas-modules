
# README

## Generate all documents

Assume module root directory is `/Users/xiaolin/tmp/datacanvas-modules/modules`. And we assume
the modules directory looks like this:

```
$ tree . -d 1
.
├── R
├── automl_2.5
├── classifier_regressor_cluster
├── customer_churn_python
├── deep_learning
├── jd_login
├── mnist
├── nlp
├── preprocessing_featureselect
├── pyspark_2.4
├── qingdao
├── tuning_prediction_metrics_release_visual
└── utils_SQL_dataframe
│   ├── CSV2PKLUnivSPy3.tar
│   ├── CSV2PKLUnivSPy3_preset.json
│   ├── ...
│   ├── SplitFeatSPy3.tar
│   └── SplitFeatSPy3_preset.json
```

Now, we can generate all markdown documents looks like this:

```sh
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir mnist
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir jd_login
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir R
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir deep_learning
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir customer_churn_python
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir preprocessing_featureselect
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir qingdao
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir classifier_regressor_cluster
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir tuning_prediction_metrics_release_visual
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir nlp
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir pyspark_2.4
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir utils_SQL_dataframe
python generate_modules_markdown.py --root /Users/xiaolin/tmp/datacanvas-modules/modules --dir automl_2.5
```

## Serve documents

```sh
mkdocs serve
```

## Reference

- mkdocs: https://github.com/mkdocs/mkdocs

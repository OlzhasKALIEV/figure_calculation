from pyspark.sql import SparkSession

# Создание SparkSession
spark = SparkSession.builder \
    .appName("Product Category Join") \
    .getOrCreate()

# Создание датафрейма продуктов
products_data = [("product1", "category1"),
                ("product2", "category2"),
                ("product3", "category1")]

products_df = spark.createDataFrame(products_data, ["product", "category"])

# Создание датафрейма категорий
categories_data = [("category1", "Category 1"),
                   ("category2", "Category 2"),
                   ("category3", "Category 3")]

categories_df = spark.createDataFrame(categories_data, ["category", "category_name"])

# Присоединение датафреймов по столбцу "category"
result_df = products_df.join(categories_df, "category", "left")

# Отображение результирующего датафрейма
result_df.show()
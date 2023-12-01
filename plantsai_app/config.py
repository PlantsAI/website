import os


upload_folder = "./static/uploads"
weights_path = "./weights/best.onnx"
image_size = 224
thread = 4
allowed_extensions = {'bmp', 'png', 'jpg', 'jpeg'}


# Database
database_name = "postgres"
database_uri = 'postgresql://root:XmXx8f6U4jex4DvcTbGTrtep@alfie.iran.liara.ir:32346/postgres'

classes_names = ["bluebell", "buttercup", "coltsfoot", "cowslip", "crocus", "daffodil", "daisy", "dandelion", "fritillary", 
                 "iris", "lilyvalley", "pansy", "snowdrop", "sunflower", "tigerlily", "tulip", "windflower"]

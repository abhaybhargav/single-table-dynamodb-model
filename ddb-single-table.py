import boto3
from boto3.dynamodb.conditions import Attr, Key

db = boto3.resource("dynamodb")
table = db.Table("single-table")

def create_image(image_name, image_id):
    """
    1. Check for the image (exists) => pk(image_name), sk.begins_with("v_")
    2. Increment Version or create new image
    """
    existing_images = table.query(KeyConditionExpression = Key("pk").eq(image_name) & Key("sk").begins_with("v_"))
    if 'Items' in existing_images and existing_images.get('Items'):
        num_versions = len(existing_images.get('Items'))
        table.put_item(Item={"pk": image_name, "sk": "v_{}".format(num_versions + 1), "image_id": image_id})
        table.put_item(Item={"pk": "image", "sk": "v0#{}".format(image_name), "image_id": image_id})
    else:
        table.put_item(Item={"pk": image_name, "sk": "v_1", "image_id": image_id})
        table.put_item(Item={"pk": "image", "sk": "v0#{}".format(image_name), "image_id": image_id})

def list_latest_images():
    list_images = table.query(KeyConditionExpression=Key("pk").eq("image") & Key("sk").begins_with("v0#"))
    print(list_images.get('Items'))

def get_latest_image_by_name(image_name):
    specific = table.get_item(Key = {"pk": "image", "sk": f"v0#{image_name}"})
    print(specific.get('Item'))

def get_specific_image_by_name_and_version(image_name, version):
    older_version = table.get_item(Key = {"pk": image_name, "sk": f"v_{version}"})
    print(older_version.get('Item'))
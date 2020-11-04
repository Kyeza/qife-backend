from django.utils.text import slugify


def get_image_filename(instance, filename):
    username = instance.owner.username
    slug = slugify(username)
    return f'item_images/{slug}-{filename}'

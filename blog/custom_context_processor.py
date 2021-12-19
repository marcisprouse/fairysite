from blog.models import Post
from taggit.models import Tag
import random



def posts_renderer(request):
    all_posts = Post.objects.all()
    pub_posts = Post.objects.all().filter(status="published")
    all_posts_list = []
    palette = []

    for post in all_posts:
        all_posts_list.append(post)

    for p in all_posts_list:
        random_number = random.randint(0,16777215)
        hex_number =format(random_number,'x')
        hex_number = '#'+hex_number
        palette.append(hex_number)

    retval = {'all_posts':all_posts,
              'palette':palette,
              'pub_posts':pub_posts
              }
    return retval;


def tag_renderer(request):
    all_tags = Tag.objects.all()
    retval = {'all_tags': all_tags}
    return retval;

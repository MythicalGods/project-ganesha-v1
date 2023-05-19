from entities.post import Post

class PostRepository:
    def __init__(self):
        self._posts = [
            {
                'author': 'Corey Schafer',
                'title': 'Blog Post 1',
                'content': 'First post content',
                'date_posted': 'April 20, 2018'
            },
            {
                'author': 'Jane Doe',
                'title': 'Blog Post 2',
                'content': 'Second post content',
                'date_posted': 'April 21, 2018'
            }
        ]

    def get_all(self):
        return list(map(
            lambda post: Post.from_dict(post),
            self._posts
        ))
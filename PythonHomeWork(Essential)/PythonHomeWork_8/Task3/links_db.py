from urllib.parse import urlparse
import os.path
import shelve


class LinksDB(object):
    """Storage of the links"""

    def __init__(self):
        self._db_name = os.path.join('database', 'links_db')

    def get_url(self, name):
        """метод получения ссілки по имени.
        Выбрасывает KeyError, если имя не найденою."""

        with shelve.open(self._db_name) as db:
            return db[name]

    def set_url(self, name, url):
        """Method of adding new link.
        Give KeyError, if name already exist.
        Give the ValueError, if URl empty or incorrect"""

        url = self.normalize_url(url)

        if not name:
            raise KeyError('Link name cannot be empty',  name)
        if not url:
            raise ValueError('Invalid link URL', url)

        with shelve.open(self._db_name) as db:
            if name in db:
                raise KeyError('Link already exist', name)
            db[name] = url

    def normalize_url(self, url):
        """Method add protocol, if protocol doesnt exist.
        and returns corrected or source URL(if this URL are correct) or
        return None"""

        if not urlparse(url).scheme:
            url = 'http://' + url
        if urlparse(url).netloc:
            return url
        else:
            return None

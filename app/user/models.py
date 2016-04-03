from app.common import Base, db, StringEnum
from werkzeug.utils import cached_property


class User(Base):
    __tablename__ = 'users'

    nickname = db.Column(db.String(100))
    realname = db.Column(db.String(100))
    bio = db.Column(db.Text())
    avatar_media_id = db.Column(db.BigInteger)


class Media(Base):
    """
    qiniu based media object
    """
    __tablename__ = 'medias'

    bucket = db.Column('storage_bucket', db.String(255), nullable=False)
    key = db.Column('storage_key', db.String(255), nullable=False)
    mime_type = db.Column(db.String(128), nullable=False)
    image_width = db.Column(db.Integer)
    image_height = db.Column(db.Integer)
    origin_uri = db.Column(db.String(2038))

    @cached_property
    def url(self):
        qiniu_hosts = {

        }
        host = qiniu_hosts[self.bucket]
        return 'http://%s/%s' % (host, self.key)

    def url_with_size(self, width, height, fmt='jpeg'):
        if self.url:
            return '%s?imageView2/1/w/%s/h/%s/format/%s' % (self.url, width, height, fmt)


class Oauth(Base):
    __tablename__ = 'oauth'
    __table_args__ = (
        db.UniqueConstraint('site', 'site_user_uid'),
        db.Index('oauth_user_idx', 'user_id'),
    )

    class Site(StringEnum):
        wechat = 'wechat'

    user_id = db.Column(db.BigInteger)
    site_app_id = db.Column(db.String(255))
    site = db.Column(db.Enum(*Site.values(), name='oauth_site'), nullable=False)
    access_token = db.Column(db.Text)
    refresh_token = db.Column(db.Text)
    expires_at = db.Column(db.DateTime(True))
    site_user_uid = db.Column(db.String(255), nullable=False)
    wechat_union_id = db.Column(db.String(255))
    site_user_name = db.Column(db.String(255))
    site_user_location = db.Column(db.String(255))
    site_user_avatar_url = db.Column(db.String(2038))
    site_user_bio = db.Column(db.String(255))

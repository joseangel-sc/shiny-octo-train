CREATE TABLE views (
  id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
  viewer_id MEDIUMINT UNSIGNED NOT NULL,
  post_id MEDIUMINT UNSIGNED NOT NULL,
  PRIMARY KEY (id)  
);

CREATE TABLE posts (
  id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
  post_text varchar(255) NOT NULL,
  times_seen int default 0,
  author_id MEDIUMINT UNSIGNED NOT NULL,
  PRIMARY KEY (id)  
);

CREATE TABLE user (
  id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
  username varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  profile_pic varchar(255) NOT NULL,
  user_type varchar(255) NOT NULL,
  user_password varchar(255) NOT NULL,
  PRIMARY KEY (id)  
);


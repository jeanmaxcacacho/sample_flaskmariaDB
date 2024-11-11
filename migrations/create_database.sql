create database if not exists samplecrud_db;
use samplecrud_db;

create table if not exists users(
    user_id int auto_increment primary key,
    username varchar(50) not null,
    passkey varchar(255) not null,
    created_at timestamp default current_timestamp
);

create table if not exists posts(
    post_id int auto_increment primary key,
    content text not null,
    posted_at timestamp default current_timestamp,
    user_id int,
    foreign key (user_id) references users(user_id) on delete cascade
);

insert ignore into users(username, passkey) VALUES
("user1", "samplepassword1"),
("user2", "samplepassword2");

insert ignore into posts(content, user_id) VALUES
("sample post content 1", 1),
("sample post content 2", 2);
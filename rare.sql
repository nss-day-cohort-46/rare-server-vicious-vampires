CREATE TABLE "User" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscription" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  "ended_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Post" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "content" varchar,
  "approved" bit
);

CREATE TABLE "Comment" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  "created_on" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reaction" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
 );

CREATE TABLE "PostReaction" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tag" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTag" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Category" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Category ('label') VALUES ('News');
INSERT INTO Tag ('label') VALUES ('JavaScript');
INSERT INTO Reaction ('label') VALUES ('happy');
INSERT INTO User ('first_name', 'last_name', 'email', 'bio', 'username', 'password', 'created_on', 'active') VALUES ('Tim', 'Timmons', 'tim@timmons.com', 'tall guy', 'ttimmons', 'tim123', '2021-10-10', True);
INSERT INTO Comment ('post_id', 'author_id', 'content', 'created_on') VALUES (1, 1, 'milk', '2021-10-10');
INSERT INTO Subscription ('follower_id', 'author_id', 'created_on', 'ended_on') VALUES (1, 1, '2021-10-1', '2021-10-10');
INSERT INTO DemotionQueue ('action', 'admin_id', 'approver_one_id') VALUES ('run', 1, 1);
INSERT INTO PostReaction ('user_id', 'reaction_id', 'post_id') VALUES (1, 1, 1);
INSERT INTO PostTag ('post_id', 'tag_id') VALUES (1, 1);
INSERT INTO Post ('user_id', 'category_id', 'title', 'publication_date', 'content', 'approved') VALUES (1, 1, 'mood', '2021-31-3', 'who knows', True);

DROP TABLE Category
DROP TABLE Tag
DROP TABLE Reaction
DROP TABLE User
DROP TABLE Comment
DROP TABLE Subscription




DROP TABLE Users
DROP TABLE DemotionQueue
DROP TABLE Subscriptions
DROP TABLE Post
DROP TABLE Comments
DROP TABLE Reactions
DROP TABLE PostReactions
DROP TABLE Tags
DROP TABLE PostTags
DROP TABLE Categories

-- Step 1 Hilight and drop all tables on 98-106
-- Stept 2 Hilight and Re-create all tables on 1-84. Make sure all table names are changed to Singular
-- Step 3 Hilight all of the INSERT statements on 86-95 and run


SELECT u.id
FROM User u
WHERE u.email = 'tim@timmons.com' AND u.password = 'tim123'
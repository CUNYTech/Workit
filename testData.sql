INSERT INTO users(username,email,password,firstName,lastName)
	VALUES("bob123","bob123@email.com","1234567","Bob","TheBuilder");

INSERT INTO users(username,email,password,firstName,lastName)
	VALUES("dory69","dory69@email.com","6969","Dora","TheExplorer");

INSERT INTO users(username,email,password,firstName,lastName)
	VALUES("sexySatan","sexyhoe@email.com","licky","Jerry","McFaggot");

INSERT INTO users(username,email,password,firstName,lastName)
	VALUES("blazeit420","420life@email.com","420420","Rob","Stoneson");

INSERT INTO dates(_datetime)
	VALUES(STR_TO_DATE('02-17-2018 02:00:PM','%m-%d-%Y %H:%i:%p'));

INSERT INTO dates(_datetime)
	VALUES(STR_TO_DATE('02-18-2018 03:00:PM','%m-%d-%Y %H:%i:%p'));

INSERT INTO dates(_datetime)
	VALUES(STR_TO_DATE('02-19-2018 03:30:PM','%m-%d-%Y %H:%i:%p'));

INSERT INTO dates(_datetime)
	VALUES(STR_TO_DATE('02-20-2018 04:30:PM','%m-%d-%Y %H:%i:%p'));

INSERT INTO dates(_datetime)
	VALUES(STR_TO_DATE('02-21-2018 05:30:PM','%m-%d-%Y %H:%i:%p'));

INSERT INTO dates(_datetime)
	VALUES(STR_TO_DATE('02-21-2018 06:30:PM','%m-%d-%Y %H:%i:%p'));

INSERT INTO dates(_datetime)
	VALUES(STR_TO_DATE('02-21-2018 06:30:PM','%m-%d-%Y %H:%i:%p'));

INSERT INTO dates(_datetime)
	VALUES(STR_TO_DATE('02-21-2018 02:30:PM','%m-%d-%Y %H:%i:%p'));

INSERT INTO workoutName(name)
	VALUES("chest");

INSERT INTO workoutName(name)
	VALUES("back");

INSERT INTO workoutName(name)
	VALUES("cardio");

INSERT INTO workoutName(name)
	VALUES("yoga");

INSERT INTO workoutName(name)
	VALUES("swimming");

INSERT INTO workoutName(name)
	VALUES("shoulders");

INSERT INTO workoutUserDateJoin(user_id, workoutName_id, date_id)
VALUES(SELECT id FROM users WHERE username = "bob123", 
		SELECT id FROM dates WHERE _datetime = STR_TO_DATE('02-18-2018 03:00:PM','%m-%d-%Y %H:%i:%p'),
		SELECT id FROM workoutNames WHERE name = "chest");

INSERT INTO workoutUserDateJoin(user_id, workoutName_id, date_id)
VALUES(SELECT id FROM users WHERE username = "bob123", 
		SELECT id FROM dates WHERE _datetime = STR_TO_DATE('02-21-2018 02:30:PM','%m-%d-%Y %H:%i:%p'),
		SELECT id FROM workoutNames WHERE name = "yoga");

INSERT INTO workoutUserDateJoin(user_id, workoutName_id, date_id)
VALUES(SELECT id FROM users WHERE username = "dory69", 
		SELECT id FROM dates WHERE _datetime = STR_TO_DATE('02-21-2018 06:30:PM','%m-%d-%Y %H:%i:%p'),
		SELECT id FROM workoutNames WHERE name = "cardio");

INSERT INTO workoutUserDateJoin(user_id, workoutName_id, date_id)
VALUES(SELECT id FROM users WHERE username = "blazeit420", 
		SELECT id FROM dates WHERE _datetime = STR_TO_DATE('02-20-2018 04:30:PM','%m-%d-%Y %H:%i:%p'),
		SELECT id FROM workoutNames WHERE name = "shoulders");

INSERT INTO workoutUserDateJoin(user_id, workoutName_id, date_id)
VALUES(SELECT id FROM users WHERE username = "sexySatan", 
		SELECT id FROM dates WHERE _datetime = STR_TO_DATE('02-21-2018 05:30:PM','%m-%d-%Y %H:%i:%p'),
		SELECT id FROM workoutNames WHERE name = "back");

INSERT INTO workoutUserDateJoin(user_id, workoutName_id, date_id)
VALUES(SELECT id FROM users WHERE username = "sexySatan", 
		SELECT id FROM dates WHERE _datetime = STR_TO_DATE('02-17-2018 02:00:PM','%m-%d-%Y %H:%i:%p'),
		SELECT id FROM workoutNames WHERE name = "swimming");
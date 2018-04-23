import requests
import json

# data to post
newUser = {
			"username": "bob123",
			"email": "bob123@email.com",
			"password": "1234567",
			"fname": "Bob",
			"lname": "TheBuilder",
			"gender": "male",
			"height": 5.6,
			"heightUnit": "ft",
			"weight": 156.0,
			"weightUnit": "lb",
			"bmi": 20.0 
		}

newWorkouts = [
		#1
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#2
		{
			"username" : "bob123", 
			"date": "18-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#3
		{
			"username" : "bob123", 
			"date": "20-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#4
		{
			"username" : "bob123", 
			"date": "21-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#5
		{
			"username" : "bob123", 
			"date": "19-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#6
		{
			"username" : "bob123", 
			"date": "22-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#7
		{
			"username" : "bob123", 
			"date": "23-3-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#8
		{
			"username" : "bob123", 
			"date": "4-4-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#9
		{
			"username" : "bob123", 
			"date": "11-4-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#10
		{
			"username" : "bob123", 
			"date": "16-4-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},
		#11
		{
			"username" : "bob123", 
			"date": "23-4-2018", 
			"time": "2:00pm", 
			"workout":"chest"
		},

		]
exercises = [
		#1
	[
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "27-2-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#2
	[
		{
			"username" : "bob123", 
			"date": "18-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "18-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "18-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "18-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#3
	[
		{
			"username" : "bob123", 
			"date": "20-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "20-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "20-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "20-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#4
	[
		{
			"username" : "bob123", 
			"date": "21-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "21-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "21-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "21-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#5
	[
		{
			"username" : "bob123", 
			"date": "19-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "19-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "19-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "19-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#6
	[
		{
			"username" : "bob123", 
			"date": "22-3-2018",   
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "22-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "22-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "22-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#7
	[
		{
			"username" : "bob123", 
			"date": "23-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "23-3-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "23-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "23-3-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#8
	[
		{
			"username" : "bob123", 
			"date": "4-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "4-4-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "4-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "4-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#9
	[
		{
			"username" : "bob123", 
			"date": "11-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "11-4-2018", 
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "11-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "11-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#10
	[
		{
			"username" : "bob123", 
			"date": "16-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "16-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "16-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "16-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	],
	#11
	[
		{
			"username" : "bob123", 
			"date": "23-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "23-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell chest press"
		},
		{
			"username" : "bob123", 
			"date": "23-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "dumbbell inclined chest press"
		},

		{
			"username" : "bob123", 
			"date": "23-4-2018",
			"time": "2:00pm", 
			"workout":"chest",
			"tag": "weight lifting",
			"exerciseName" : "barbell inclined chest press"
		}
	]
]

sets = [
	#1
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 95,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 110,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 145,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 145,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 45,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 50,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 55,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 55,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 40,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 45,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 50,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 55,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 110,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 120,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 130,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "27-2-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 140,
				"weightUnit" : "lb"
			}

		],

	],

	#2
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "18-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 95,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 110,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 145,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 145,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 45,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 50,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 55,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 55,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "18-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 40,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 45,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 50,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 55,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "18-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 110,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 120,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 130,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "18-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 140,
				"weightUnit" : "lb"
			}

		]

	],
	#3
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 110,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 120,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 130,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 150,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 50,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 55,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 60,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 65,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "20-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 45,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 50,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 55,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 60,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "20-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 120,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 130,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 150,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "20-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 160,
				"weightUnit" : "lb"
			}

		]

	],
	#4
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "21-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 110,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 120,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 130,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 150,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "21-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 50,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 55,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 60,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 65,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "21-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 45,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 50,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 55,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 60,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "21-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 120,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 130,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 150,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "21-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 160,
				"weightUnit" : "lb"
			}

		]

	],
	#5
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "19-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 145,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 150,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 160,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 170,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "19-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 60,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 65,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 70,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 75,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "19-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 55,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 60,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 65,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 70,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "19-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 135,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 145,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 155,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "19-3-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 165,
				"weightUnit" : "lb"
			}

		]

	],
	#6
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 145,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 150,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 160,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 170,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "22-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 60,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 65,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 70,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 75,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 55,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 60,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 65,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 70,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "22-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 135,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 145,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 155,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "22-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 165,
				"weightUnit" : "lb"
			}

		]

	],
	#7
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "23-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 155,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 175,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 180,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "23-3-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 65,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 70,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 75,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 80,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "23-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 60,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 65,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 70,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 75,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "23-3-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 145,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 155,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "23-3-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 175,
				"weightUnit" : "lb"
			}

		]

	],
	#8
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "4-4-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 155,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 175,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 180,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "4-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 65,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 70,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 75,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 80,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "4-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 60,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018",
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 65,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 70,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 75,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "4-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 145,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 155,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "4-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 175,
				"weightUnit" : "lb"
			}

		]

	],
	#9
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "11-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 175,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 185,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 195,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "11-4-2018",    
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 75,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 85,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 90,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 95,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "11-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 70,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 75,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 75,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018",    
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 80,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "11-4-2018",    
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 155,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 175,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "11-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 180,
				"weightUnit" : "lb"
			}

		]

	],
	#10
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",    
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 175,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 185,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 195,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "16-4-2018",     
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 75,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 85,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 90,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 95,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "16-4-2018",    
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 70,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 75,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 75,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",     
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 80,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "16-4-2018",     
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 155,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 175,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 180,
				"weightUnit" : "lb"
			}

		]

	],
	#11
	[	#exercise#1
		[
			{
				"username" : "bob123", 
				"date": "23-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 180,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",    
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 185,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 190,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 195,
				"weightUnit" : "lb"
			}

		],
		#exercise#2
		[
			{
				"username" : "bob123", 
				"date": "16-4-2018",     
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 85,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 95,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 105,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 110,
				"weightUnit" : "lb"
			}

		],
		#exercise#3
		[
			{
				"username" : "bob123", 
				"date": "16-4-2018",    
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 80,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018", 
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 90,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 100,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",     
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "dumbbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 110,
				"weightUnit" : "lb"
			}

		],
		#exercise#4
		[
			{
				"username" : "bob123", 
				"date": "16-4-2018",     
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 1,
				"reps" : 10,
				"weight" : 165,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 2,
				"reps" : 8,
				"weight" : 175,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",   
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 3,
				"reps" : 6,
				"weight" : 185,
				"weightUnit" : "lb"
			},
			{
				"username" : "bob123", 
				"date": "16-4-2018",  
				"time": "2:00pm", 
				"workout":"chest",
				"tag": "weight lifting",
				"exerciseName" : "barbell inclined chest press",
				"setNum" : 4,
				"reps" : 6,
				"weight" : 190,
				"weightUnit" : "lb"
			}

		]

	]

]


newUserUrl = "http://127.0.0.1:5000/user/new"
newWorkoutUrl = "http://127.0.0.1:5000/date/new/workout"
newExercise = "http://127.0.0.1:5000/date/new/exercise"
newSet = "http://127.0.0.1:5000/date/new/exercise/set"

class PostToApi():
	def __init__(self, url, jsonPost):
		self.url = url
		self.jsonPost = json.dumps(jsonPost)

	def post(self):
		request = requests.post(self.url, json= self.jsonPost)
		return request.status_code



# create new user

user = PostToApi(newUserUrl, newUser)
user.post()

for workout in newWorkouts:
	newWorkout = PostToApi(newWorkoutUrl, workout)
	newWorkout.post()

for exercise in exercises:
	for exer in exercise:
		postExercise = PostToApi(newExercise, exer)
		postExercise.post()

for s in sets:
	for a in s:
		postSets = PostToApi(newSet, a)
		postSets.post()
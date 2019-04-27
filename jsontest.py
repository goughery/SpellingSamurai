import json
dic = """{
	"version": "1.0",
	"session": {
		"new": false,
		"sessionId": "amzn1.echo-api.session.0c2e1204-8aab-44a1-8f49-814301926327",
		"application": {
			"applicationId": "amzn1.ask.skill.50c6599a-5116-41b9-8146-eabb649212d4"
		},
		"user": {
			"userId": "amzn1.ask.account.AHFB5ISVIS5F6SYAGLDEVEV3G5GHZ5MXVKSVC6RAJJBNFT2335CDTO3D7CUDBXLQ6MZGOH3DMW5EHM7PZDVNPFTN4A2DLSJ4JLJKCSBREVS7HQ5WV6LUYD6TR7R37ZAUB2F2QL423ZAYLOWW33OLAUA3KPWBCRO52FAWSU72I74WJBWWXY6JH4EUN6H7ZGFQHJGN5E5WQJHUNLI"
		}
	},
	"context": {
		"System": {
			"application": {
				"applicationId": "amzn1.ask.skill.50c6599a-5116-41b9-8146-eabb649212d4"
			},
			"user": {
				"userId": "amzn1.ask.account.AHFB5ISVIS5F6SYAGLDEVEV3G5GHZ5MXVKSVC6RAJJBNFT2335CDTO3D7CUDBXLQ6MZGOH3DMW5EHM7PZDVNPFTN4A2DLSJ4JLJKCSBREVS7HQ5WV6LUYD6TR7R37ZAUB2F2QL423ZAYLOWW33OLAUA3KPWBCRO52FAWSU72I74WJBWWXY6JH4EUN6H7ZGFQHJGN5E5WQJHUNLI"
			},
			"device": {
				"deviceId": "amzn1.ask.device.AGWL4AZTYTB4KWMYZIZJQQZHWHKKW53YQP4EY4SYF5TD67ESYU5TIIDS5T7VJYNIQNCNXFPJ3Z3VDSAB2MC5GKIVQBO4AMPJXXOQVO2UEBJJHMIN5VOBBOHPTUQBIBG5ALB7IVQTCTAWKQDHNLUEVNT4XGKSICTQBFFD2LE74NJ6NTYRZ57IE",
				"supportedInterfaces": {}
			},
			"apiEndpoint": "https://api.amazonalexa.com",
			"apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjUwYzY1OTlhLTUxMTYtNDFiOS04MTQ2LWVhYmI2NDkyMTJkNCIsImV4cCI6MTU0NTY2NzI0NywiaWF0IjoxNTQ1NjYzNjQ3LCJuYmYiOjE1NDU2NjM2NDcsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUdXTDRBWlRZVEI0S1dNWVpJWkpRUVpIV0hLS1c1M1lRUDRFWTRTWUY1VEQ2N0VTWVU1VElJRFM1VDdWSllOSVFOQ05YRlBKM1ozVkRTQUIyTUM1R0tJVlFCTzRBTVBKWFhPUVZPMlVFQkpKSE1JTjVWT0JCT0hQVFVRQklCRzVBTEI3SVZRVENUQVdLUURITkxVRVZOVDRYR0tTSUNUUUJGRkQyTEU3NE5KNk5UWVJaNTdJRSIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFIRkI1SVNWSVM1RjZTWUFHTERFVkVWM0c1R0haNU1YVktTVkM2UkFKSkJORlQyMzM1Q0RUTzNEN0NVREJYTFE2TVpHT0gzRE1XNUVITTdQWkRWTlBGVE40QTJETFNKNEpMSktDU0JSRVZTN0hRNVdWNkxVWUQ2VFI3UjM3WkFVQjJGMlFMNDIzWkFZTE9XVzMzT0xBVUEzS1BXQkNSTzUyRkFXU1U3Mkk3NFdKQldXWFk2Skg0RVVONkg3WkdGUUhKR041RTVXUUpIVU5MSSJ9fQ.aQSshzP2aoBSeFfYJmMdrRYhw0vON9RfOnLP_6gvT_9kOH_R6_0UXAyq1d4fDxnP2dTBGaz9kblazYA-qCxvALRNi82N16aA2ghuY7hacpAZVSySR0B3zRCqxKkH7nosMwVY2mtquzgPojVDDEe5f9_yNWG1KsiN2OHnF2f115y6P-vfQY2MloZls6UYJZC5983sAXNRvQMdeDtESr1YU9V_ghdqp7RYr61cY1mmthIg2si9BeMLAiMPtPfdULpBJ7NaSpB0lYS3oFqIsN6S87taFEMqu7uEO4CkhtF-A2tKjMPM7o1jUmJaqpUZc490t3tipfHRCa6M_V1Qo7XRHw"
		},
		"Viewport": {
			"experiences": [
				{
					"arcMinuteWidth": 246,
					"arcMinuteHeight": 144,
					"canRotate": false,
					"canResize": false
				}
			],
			"shape": "RECTANGLE",
			"pixelWidth": 1024,
			"pixelHeight": 600,
			"dpi": 160,
			"currentPixelWidth": 1024,
			"currentPixelHeight": 600,
			"touch": [
				"SINGLE"
			]
		}
	},
	"request": {
		"type": "IntentRequest",
		"requestId": "amzn1.echo-api.request.f7c6be79-0e32-45f2-8120-72632ebed7bf",
		"timestamp": "2018-12-24T15:00:47Z",
		"locale": "en-US",
		"intent": {
			"name": "AddWordsIntent",
			"confirmationStatus": "NONE",
			"slots": {
				"ListNumber": {
					"name": "ListNumber",
					"value": "1",
					"resolutions": {
						"resolutionsPerAuthority": [
							{
								"authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.50c6599a-5116-41b9-8146-eabb649212d4.ListNumber",
								"status": {
									"code": "ER_SUCCESS_MATCH"
								},
								"values": [
									{
										"value": {
											"name": "one",
											"id": "f97c5d29941bfb1b2fdab0874906ab82"
										}
									}
								]
							}
						]
					},
					"confirmationStatus": "NONE",
					"source": "USER"
				}
			}
		},
		"dialogState": "IN_PROGRESS"
	}
}"""

dic = json.loads(dic)

print(dic['request']['intent']['slots']['ListNumber']['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name'])

from gpiozero import MotionSensor

pir = MotionSensor(21)

while True:
	pir.wait_for_motion()
	print("Ada Gerakan")
	pir.wait_for_no_motion()
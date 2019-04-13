import logging
from gpiozero import MotionSensor
from picamera import PiCamera

from datetime import datetime
import time

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(
            format='%(asctime)s %(levelname)-8s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')

camera = PiCamera()
pir = MotionSensor(4)
try:
    while True:
        logging.info("Waiting for motion...")
        pir.wait_for_motion()
        logging.info("Motion detected....")
        filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
        logging.info("Capturing....")
        camera.capture(filename)
        logging.info("Waiting for no motion....")
        pir.wait_for_no_motion()
        #logging.info("Stop preview.....") 
        #camera.stop_preview()
        logging.info("Sleeping....")
        time.sleep(0.5)
except Exception as ex:
    logging.error(ex)        
finally:
    logging.info("Closing camera...")
    camera.close()


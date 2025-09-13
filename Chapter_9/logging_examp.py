
# The Digital Journal

import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
def track_mission_progress(mission_status):
    if mission_status == "start":
        logging.info("Mission has begun. May the Force be with you.")
    elif mission_status == "warning":
        logging.warning("Energy shields are failing!")
    elif mission_status == "failure":
        logging.error("Mission failed. A bug was encountered.")







        
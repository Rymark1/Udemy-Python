from prescription_data import *

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    presription = patients[patient]
    # if warfarin in presription:
    #     presription.remove(warfarin)
    #     presription.add(edoxaban)
    # else:
    #     print(f"Patient {patient} is not taking Warfarin."
    #           f" Please remove {patient} from the trial.")

    try:
        presription.remove(warfarin)
        presription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin."
              f" Please remove {patient} from the trial.")

    print(patient, presription)

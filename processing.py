def transform_names(channels):
    if channels is not None:
        transforms = {"Northernlion": "NL", "DanGheesling": "DanG", "Jerma985": "Jerma", "meat": "meat<3"}
        return [transforms[channel] if channel in transforms else channel for channel in channels]

    return channels

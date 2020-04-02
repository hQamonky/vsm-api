# vsm-api
## Description
QMK Virtual Sound Mixer API is a REST API that enables you to control a linux pulseaudio sound server.
## Usage
All responses will have the form 
```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`.

### List sinks

**Definition**

`GET /sinks`

**Response**

- `200 OK` on success

```json
[
    {
        "id": "0",
        "name": "line-out",
        "driver": "alsa-card",
        "sample-description": "2ch",
        "state": "IDLE"
    },
    {
        "id": "1",
        "name": "roccat",
        "driver": "alsa-card",
        "sample-description": "2ch",
        "state": "IDLE"
    }
]
```


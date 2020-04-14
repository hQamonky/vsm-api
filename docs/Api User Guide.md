# vsm-api
## Description
QMK Virtual Sound Mixer API is a REST API coded in Python that exposes commands to control a linux pulseaudio sound server.
## Usage
All responses will have the form 
```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

## Endpoints  

### Cards

```
- /cards  
- /card/<string:card>/set-profile/<string:profile>  
```

### Modules

#### `/load-module/<string:name>`  
The `name` parameter is the name of the module.  
This is a post request that takes the following body in json :
```json 
{  
    "latency_msec": "1",  
    "source": "source_name",  
    "sink": "sink_name"  
}
```  
The return value is the index of the module that was just loaded, to be used as a parameter to unload it later.

#### `/unload-module/<string:identifier>`  

The identifier parameter has to be the index returned by the `load-module` endpoint.  

### Sinks

```
- /sinks  
- /sink/<string:sink>/set-default  
- /sink/<string:sink>/set-port/<string:port>  
- /sink/<string:sink>/set-volume-percentage/<string:volume>  
- /sink/<string:sink>/set-mute/<string:mute>  
```

### Sink inputs

```
- /sink-input/<string:sink_input>/set-volume-percentage/<string:volume>  
- /sink-input/<string:sink_input>/set-mute/<string:mute>  
```

### Sources

```
- /sources  
- /source/<string:source>/set-default  
- /source/<string:source>/set-port/<string:port>  
- /source/<string:source>/set-volume-percentage/<string:volume>  
- /source/<string:source>/set-mute/<string:mute>  
```

### Source outputs

```
- /source-output/<string:source_output>/set-volume-percentage/<string:volume>  
- /source-output/<string:source_output>/set-mute/<string:mute>  
```

### Clients

```
- /clients  
```

### Native methods

These endpoints are getters that return the raw values of the bash command, without any processing.

```
- /native/stats  
- /native/info  
- /native/clients  
- /native/clients-full  
- /native/sinks  
- /native/sinks-full  
- /native/sink-inputs  
- /native/sources  
- /native/sources-full  
- /native/source-outputs  
- /native/cards  
- /native/cards-full  
- /native/modules  
```

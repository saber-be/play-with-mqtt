Lets Play with MQTT

# Create GGV2 Component

```
sudo /greengrass/v2/bin/greengrass-cli deployment create   
    --recipeDir $recipe_dir  
    --artifactDir $artifacts_dir           
    --merge "$component=$version"
```

## example (hello component)
```
sudo /greengrass/v2/bin/greengrass-cli deployment create   
    --recipeDir /home/saber/python/mqtt/pubsub/gg-components/recipe  
    --artifactDir /home/saber/python/mqtt/pubsub/gg-components/artifacts           
    --merge "com.example.hello=1.0.0"
```

# Check GG logs

```
sudo tail -n 40  /greengrass/v2/logs/greengrass.log
```

# Check component log

```
sudo tail -n 40  /greengrass/v2/logs/com.example.hello.log
```



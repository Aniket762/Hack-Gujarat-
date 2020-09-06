public class ObjectSpawner : MonoBehaviour
{
    public GameObject objectToSpawn;
    private PlacementIndicator placementIndicator;

    void Start()
    {
        placementIndicator=FindObjectOfType<PlacementIndicator>();
    }

    void Update()
    {
        if(Input.touchCount==1){
            GameObject obj=Instantiate(objectToSpawn,placementIndicator.transform.position,
                placementIndicator.transform.rotation);
        }
        
    }
}
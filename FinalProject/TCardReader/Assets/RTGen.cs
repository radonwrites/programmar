using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
[System.Runtime.InteropServices.ComVisible(true)]
[System.Serializable]
//public class Random

public class RTGen : MonoBehaviour
{
    //public GameObject randomWord;
    //public Font font;
    //public var Word;
    // Start is called before the first frame update
    void Start()
    {
        // do I need ForceMeshUpdate() function for TMP?
        // Im testing with both mesh types TextMesh and TMP at the same time, not sure if good idea?
        GetComponent<TextMesh>().text = "testing";
        //GameObject randomWord;
        //TextMesh word = GameObject.GetComponent<TextMeshPro>();

        //word.text = "hello!";

        /*
        //getting this from Unity documentation on TextGenerator
        //working from the ground up because I get errors I don't understand when building off the UI 
        TextGenerationSettings settings = new TextGenerationSettings();
        settings.textAnchor = TextAnchor.MiddleCenter;
        settings.color = Color.red;
        settings.generationExtents = new Vector2(500.0F, 200.0F);
        settings.pivot = Vector2.zero;
        settings.richText = true;
        settings.font = font;
        settings.fontSize = 32;
        settings.fontStyle = FontStyle.Normal;
        settings.verticalOverflow = VerticalWrapMode.Overflow;
        TextGenerator generator = new TextGenerator();
        generator.Populate("I am a string", settings);
        Debug.Log("I generated: " + generator.vertexCount + " verts!");
        */
    }

    // Update is called once per frame
}

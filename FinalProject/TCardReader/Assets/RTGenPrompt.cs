using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using System;
[System.Runtime.InteropServices.ComVisible(true)]
[System.Serializable]

public class RTGenPrompt : MonoBehaviour
{
    void Start()
    {
        System.Random rnd = new System.Random();
        string[] prompts = { "Riverside", "A lost memory", "The one who waited", "Never alone", 
                            "Fronds", "Unopened pickle jar", "Rainbows aren't real", "Cold dinner"};                                      

        int pIndex = rnd.Next(prompts.Length);

        GetComponent<TextMesh>().text = prompts[pIndex];
    }
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using System;
[System.Runtime.InteropServices.ComVisible(true)]
[System.Serializable]

public class RTGenPhrase : MonoBehaviour
{
    void Start()
    {
        System.Random rnd = new System.Random();
        string[] phrase = { "a little lost", "he nodded", "I thought so", "frantic, racing", 
                            "shrugging, she", "sopping wet", "not knowing what to expect",
                            "all over the place", "it was fine", "not panicking", "no worries"};                                      

        int phIndex = rnd.Next(phrase.Length);

        GetComponent<TextMesh>().text = phrase[phIndex];
    }
}

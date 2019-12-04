using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextAppear : MonoBehaviour {
    int word = 0;
    string[] options = new string[]{"test", "idk"};

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        string thisword = word[Random.Word(options)];
        return thisword;
    }
}


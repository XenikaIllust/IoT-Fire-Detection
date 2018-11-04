using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;


public class textDelayPrint : MonoBehaviour {
	public Text warning;
	private float nextActionTime = 0.0f;
	public float period = 0.3f;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if (Time.time > nextActionTime) {
			nextActionTime += period;
			int randomNumber = Random.Range (1,3);
			warning.text = "Fire and CO detected in <First> floor. Potential "+ randomNumber + " victim(s).";
		}
	}
}

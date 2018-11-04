using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class RandomNumberGenerator : MonoBehaviour {
	public Text temperatures;
	private float nextActionTime = 0.0f;
	public float period = 0.3f;
	// Use this for initialization
	void Start () {

	}
	
	// Update is called once per frame
	void Update () {
		if (Time.time > nextActionTime) {
			nextActionTime += period;
			int randomNumber = Random.Range (200, 205);
			Debug.Log (randomNumber);
			temperatures.text = "Floor 1 temperature: " + randomNumber.ToString ();
		}
	}
}

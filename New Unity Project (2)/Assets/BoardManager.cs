using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoardManager : MonoBehaviour
{
	// Start is called before the first frame update
	[SerializeField] Player m_player_white;
	[SerializeField ]Player m_player_red;
	List<GameObject>caselles;
	void Start()
	{
		DrawBoard();
		m_player_white = new Player(0);
		m_player_red = new Player(1);
		caselles = new List<GameObject>();
		int i = 0;
		foreach (Transform child in transform)
		{
			child.gameObject.AddComponent(typeof(Casella));
			child.gameObject.GetComponent<Casella>().m_casella_index = i;
			caselles.Add(child.gameObject);
		}
	}

    // Update is called once per frame
    void Update()
    {
        
    }
	public void drawPiece()
	{

	}
	private void DrawBoard()
	{
		Vector3 widthLine = Vector3.right * 8;
		Vector3 heightLine = Vector3.forward * 8;

		for (int i = 0; i <= 8; i++)
		{
			Vector3 start = Vector3.forward * i;
			Debug.DrawLine(start, start + widthLine);
			for (int j = 0; j <= 8; j++)
			{
				start = Vector3.right * j;
				Debug.DrawLine(start, start + heightLine);
			}
		}
	}
}

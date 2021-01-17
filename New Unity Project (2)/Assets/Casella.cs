using System.Collections;
using System.Collections.Generic;
using UnityEngine;


class Casella:MonoBehaviour
	{
	public int m_casella_index;
	public bool isUsed = false;
	public int team_index = -1;
	public int piece_index = -1;
	public GameObject piece;

	public Casella(int casella_index)
	{
		this.m_casella_index = casella_index;

	}

	public void setPiece(GameObject piece, int team_index, int peace_index)
	{
		this.piece = piece;
		this.team_index = team_index;
		this.piece_index = peace_index;
		this.isUsed = true;
	}

	public void removePiece( int team_index)
	{
		this.piece = null;
		this.isUsed = false;
		this.team_index = -1;
		this.piece_index = -1;
	}


}

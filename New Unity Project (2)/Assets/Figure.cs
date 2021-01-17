using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

[System.Serializable]
public static class LayoutGenerator
{
	private static int[,] tavern = new int[,] { { 12 } };
	private static int[,] stable = new int[,] { { 7, 12 }, { 13, 12 }, { 17, 12 }, { 11, 12 } };
	private static int[,] inn = new int[,] { { 7, 12, 13 }, { 13, 12, 17 }, { 17, 12, 11 }, { 11, 12, 7 } };
	private static int[,] bridge = new int[,] { { 7, 12, 17 }, { 13, 12, 11 } };
	private static int[,] square = new int[,] { { 6, 7, 11, 12 } };
	private static int[,] abey = new int[,] { { 7, 12, 13, 18 }, { 13, 12, 17, 16 }, { 17, 12, 11, 6 }, { 11, 12, 7, 8 } };
	private static int[,] manon = new int[,] { { 7, 11, 12, 13 }, { 7, 12, 17, 13 }, { 11, 12, 13, 17 }, { 7, 12, 17, 11 } };
	private static int[,] tower = new int[,] { { 8, 12, 16, 13, 17 }, { 6, 12, 18, 11, 17 }, { 8, 12, 16, 7, 11 }, { 6, 12, 18, 7, 13 } };
	private static int[,] infirmary = new int[,] { { 7, 12, 17, 11, 13 } };
	private static int[,] castle = new int[,] { { 6, 11, 12, 13, 8 }, { 8, 7, 12, 17, 18 }, { 11, 12, 13, 16, 18 }, { 7, 12, 17, 6, 16 } };
	private static int[,] academy = new int[,] { { 7, 12, 17, 11, 18 }, { 11, 12, 13, 7, 16 }, { 7, 12, 17, 6, 13 }, { 11, 12, 13, 17, 8 } };
	private static int[,] cathedral = new int[,] { { 7, 12, 17, 22, 11, 13 }, { 10, 11, 12, 13, 7, 17 }, { 3, 7, 12, 17, 11, 13 }, { 11, 12, 13, 14, 7, 17 } };
	public static List<int[,]> m_layouts = new List<int[,]> { tavern, stable, inn, bridge, square, abey, manon, tower, infirmary, castle, academy, cathedral };

}


[System.Serializable]
public class Figure
{
	
	public int[,] m_figure_layout;
	public int m_rotation = 0;
	public int m_team = 0;
	public int m_id = 0;
	public bool m_isUsed = false;
	public Vector2Int m_boardPosition;
	public Figure(int [,] layout, int team,int figure_id)
	{
		m_figure_layout = layout;
		m_team = team;
		m_id = figure_id;
		m_boardPosition = new Vector2Int(0, 0);
		Debug.Log("initializing Figure with id " + m_id);
	}

	public void rotate()
	{
		m_rotation = (m_rotation + 1) % m_figure_layout.Length;
	}

	public int[] getLayout()
	{
		return Enumerable.Range(0, m_figure_layout.GetLength(1))
				.Select(x => m_figure_layout[m_rotation, x])
				.ToArray();
	}

	public void setBoardPosition(Vector2Int position)
	{
		m_boardPosition = position;
	}

	public Vector2Int getBoardPosition()
	{
		return m_boardPosition;
	}

	public bool getIsUsed()
	{
		return m_isUsed;
	}
}

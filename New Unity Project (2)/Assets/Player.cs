using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class Player 
{
	

	public int m_team = 0;
	public List<Figure> m_figures;
	public int m_nFigures = 14;
	public List<int> m_figure_ids;

	public Player(int team)
	{
		m_team = team;
		m_figure_ids = new List<int>{ 0, 0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		initFigures();
		Debug.Log("initializing player with team: " + m_team);
	}

	public void initFigures()
	{
		m_figures = new List<Figure>();
		m_figure_ids.ForEach(delegate (int figure_id)
		{
			Debug.Log(figure_id);
			m_figures.Add(new Figure(LayoutGenerator.m_layouts[figure_id], m_team, figure_id));
		});
	}
}

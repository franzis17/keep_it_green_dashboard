import { useState, useEffect } from 'react'
import axios from 'axios'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts'
import { Emission, EmissionsResponse } from './types'

function App() {
  const [emissions, setEmissions] = useState<Emission[]>([])
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get<EmissionsResponse>('http://localhost:8000/api/emissions/')
        // Sort emissions by date
        const sortedEmissions = response.data.emissions.sort((a, b) => 
          new Date(a.date).getTime() - new Date(b.date).getTime()
        )
        setEmissions(sortedEmissions)
      } catch (err) {
        const errorMessage = err instanceof Error ? err.message : 'An unknown error occurred'
        setError(errorMessage)
        console.error('Error fetching data:', err)
      }
    }

    fetchData()
  }, [])

  if (error) {
    return <div>Error: {error}</div>
  }

  return (
    <div>
      <h1>Carbon Emissions Graph</h1>
      {emissions.length > 0 ? (
        <LineChart
          width={800}
          height={400}
          data={emissions}
          margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="date" 
            tickFormatter={(date) => new Date(date).toLocaleDateString()}
          />
          <YAxis />
          <Tooltip 
            labelFormatter={(date) => new Date(date).toLocaleDateString()}
            formatter={(value) => [`${Number(value).toFixed(2)} kg`, 'CO₂ Emissions']}
          />
          <Legend />
          <Line 
            type="monotone" 
            dataKey="co2_emissions" 
            stroke="#8884d8" 
            name="CO₂ Emissions"
          />
        </LineChart>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  )
}

export default App

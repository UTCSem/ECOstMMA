
import React, {useState, useEffect} from 'react'
import axios from 'axios'

function App(){
  const [players, setPlayers] = useState([])
  useEffect(()=>{
    axios.get(import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL + '/players' : 'http://localhost:8000/players')
      .then(r=> setPlayers(r.data)).catch(()=>{})
  },[])
  return (
    <div className='p-6 font-sans'>
      <h1 className='text-2xl mb-4'>MMA SaaS — Demo</h1>
      <section className='mb-6'>
        <h2 className='text-xl'>Players</h2>
        <ul>
          {players.map(p=> <li key={p.id}>{p.name} — {p.style || '—'}</li>)}
        </ul>
      </section>
      <section>
        <h2 className='text-xl'>Quick actions</h2>
        <p>Use backend to create players and experiment.</p>
      </section>
    </div>
  )
}

export default App

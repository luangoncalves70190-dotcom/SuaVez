import { Injectable } from '@nestjs/common';

@Injectable()
export class AiService {
  async answer(message: string, context: any) {
    const key = process.env.GROQ_API_KEY;
    if (!key) return { answer: this.fallbackAnswer(message, context), mode: 'assistente-integrado' };

    const model = process.env.GROQ_MODEL || 'llama-3.3-70b-versatile';
    const system = `Você é o Assistente SuaVez. Responda em português, de forma curta e clara. Você auxilia somente em informações operacionais sobre fila, posição, tempo de espera, unidade e uso do sistema. Não faça diagnóstico, não recomende medicamentos e não substitua triagem clínica. Contexto atual: ${JSON.stringify(context || {})}`;

    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${key}` },
      body: JSON.stringify({
        model,
        temperature: 0.3,
        messages: [{ role: 'system', content: system }, { role: 'user', content: message }]
      })
    });

    if (!response.ok) return { answer: this.fallbackAnswer(message, context), mode: 'fallback' };

    const data: any = await response.json();
    return {
      answer: data.choices?.[0]?.message?.content || this.fallbackAnswer(message, context),
      mode: 'groq'
    };
  }

  private fallbackAnswer(message: string, context: any) {
    const t = (message || '').toLowerCase();
    if (t.includes('posição') || t.includes('fila')) {
      return context?.position !== undefined ? `Sua posição atual é ${context.position}.` : 'Você ainda não possui uma fila ativa.';
    }
    if (t.includes('tempo') || t.includes('espera')) {
      return context?.estimatedTime !== undefined ? `A estimativa atual é de aproximadamente ${context.estimatedTime} minutos.` : 'A estimativa aparece quando você entra em uma fila.';
    }
    if (t.includes('triagem')) return 'A triagem clínica continua sendo realizada pela equipe de saúde. O SuaVez organiza somente a recepção e o acompanhamento da fila.';
    if (t.includes('medic') || t.includes('diagn')) return 'Não realizo diagnóstico nem indico medicamentos. Procure a equipe de saúde para orientação clínica.';
    return 'Posso ajudar com sua posição, tempo de espera, unidade escolhida e funcionamento do SuaVez.';
  }
}

import { Injectable } from '@nestjs/common';

@Injectable()
export class QueueService {
  private entries = new Map<string, any>();

  join(body: any) {
    const id = `Q-${Date.now()}`;
    const entry = { id, ...body, status: 'AGUARDANDO', createdAt: new Date().toISOString() };
    this.entries.set(id, entry);
    return entry;
  }

  get(id: string) {
    return this.entries.get(id) || { id, status: 'NAO_ENCONTRADO' };
  }

  leave(id: string) {
    const current = this.entries.get(id);
    if (current) this.entries.set(id, { ...current, status: 'CANCELADO' });
    return { ok: true };
  }
}

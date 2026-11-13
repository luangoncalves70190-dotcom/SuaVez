import { Body, Controller, Delete, Get, Param, Post } from '@nestjs/common';
import { QueueService } from './queue.service';

@Controller('api/queue')
export class QueueController {
  constructor(private readonly service: QueueService) {}
  @Post('join') join(@Body() body: any) { return this.service.join(body); }
  @Get(':id') get(@Param('id') id: string) { return this.service.get(id); }
  @Delete(':id') leave(@Param('id') id: string) { return this.service.leave(id); }
}

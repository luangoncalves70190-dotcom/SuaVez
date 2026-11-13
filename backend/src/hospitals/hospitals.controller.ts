import { Controller, Get } from '@nestjs/common';
import { HospitalsService } from './hospitals.service';

@Controller('api/hospitals')
export class HospitalsController {
  constructor(private readonly service: HospitalsService) {}
  @Get() findAll() { return this.service.findAll(); }
}
